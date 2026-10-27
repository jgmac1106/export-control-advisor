"""Synthetic regression tests; run with python3 -m unittest discover -s scripts/tests."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'inventory_evidence.py'
spec = importlib.util.spec_from_file_location('inventory', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / 'exports'
        self.source.mkdir()
        (self.source / 'policy.json').write_bytes(b'{"redirectprinters":0}\n')
        self.output = self.base / 'review'

    def test_hash_original_and_unknown_provenance(self):
        before = (self.source / 'policy.json').read_bytes()
        result = module.inventory(self.source, self.output, 'SYNTHETIC')
        item = result['entries'][0]
        self.assertEqual(item['sha256'], hashlib.sha256(before).hexdigest())
        self.assertEqual((self.source / 'policy.json').read_bytes(), before)
        self.assertIsNone(item['provenance']['collected_at'])
        self.assertEqual(item['review_status'], 'not_assessed')
        self.assertEqual(item['mappings'], [])
        self.assertEqual(json.loads((self.output / 'manifest.json').read_text()), result)

    def test_refuses_nested_output_and_overwrite(self):
        with self.assertRaises(ValueError):
            module.inventory(self.source, self.source / 'out', 'SYNTHETIC')
        module.inventory(self.source, self.output, 'SYNTHETIC')
        with self.assertRaises(ValueError):
            module.inventory(self.source, self.output, 'SYNTHETIC')

    def test_symlink_and_missing_metadata_are_visible(self):
        (self.source / 'outside').symlink_to(self.base)
        result = module.inventory(self.source, self.output, 'SYNTHETIC', {'missing.csv': {'collection_status':'partial'}})
        self.assertEqual(result['inventory_status'], 'with_issues')
        self.assertEqual(len(result['entries']), 1)
        self.assertEqual({x['reason'] for x in result['issues']}, {'symlink_skipped','metadata_without_inventoried_file'})

    def test_metadata_cannot_claim_verified(self):
        with self.assertRaises(ValueError):
            module.inventory(self.source, self.output, 'SYNTHETIC', {'policy.json': {'provenance_status':'verified'}})
        result = module.inventory(self.source, self.output, 'SYNTHETIC', {'policy.json': {'collection_status':'partial','source_system':'synthetic'}})
        self.assertEqual(result['entries'][0]['provenance_status'], 'user_reported')
        self.assertEqual(result['entries'][0]['provenance']['collection_status'], 'partial')

    def test_metadata_path_traversal_rejected(self):
        with self.assertRaises(ValueError):
            module.inventory(self.source, self.output, 'SYNTHETIC', {'../secret': {}})

if __name__ == '__main__':
    unittest.main()
