import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import v2_pipeline as v
class V2Tests(unittest.TestCase):
 def test_seed(self):self.assertEqual(v.generate(8,4),v.generate(8,4))
 def test_negation_normalization(self):self.assertIn("tidak",v.preprocess("GAK bagus bgt"))
 def test_sentiment_baseline(self):self.assertEqual(v.sentiment("jalan aman nyaman"),"positif")
 def test_eval_metrics(self):self.assertEqual(v.evaluate(["positif","negatif"],["positif","netral"])["accuracy"],.5)
 def test_theme_multilabel(self):self.assertGreaterEqual(len(v.themes([{"post_id":"x","text":"akses warga difabel dan bus kota"}])["theme_counts"]),2)
 def test_network_weight(self):self.assertEqual(v.network([{"author":"A","reply_to":"B"},{"author":"A","reply_to":"B"}])["edges"][0]["weight"],2)
 def test_end_to_end(self):
  with tempfile.TemporaryDirectory() as d:
   path=Path(d)/"d.csv";v.write_csv(path,v.generate(10,2));result=v.run(path,Path(d)/"out","synthetic");self.assertTrue(result["report"].exists())
if __name__=="__main__":unittest.main()
