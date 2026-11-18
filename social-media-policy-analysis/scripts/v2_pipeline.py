#!/usr/bin/env python3
"""Reproducible standard-library prototype for social-media research."""
import argparse,csv,json,re,random
from collections import Counter
from datetime import datetime,timedelta
from pathlib import Path
ACTORS=[("PemkotJogja","government"),("TransportWatch","community"),("PedagangMalioboro","merchant"),("KomunitasDifabel","community"),("MediaJogja","media"),("WisataJogja","media"),("WargaJogja","resident"),("JogjaPeduli","community"),("MalioboroHeritage","community"),("AkademisiKota","academic"),("KurirJogja","worker"),("DishubJogja","government")]
TEXTS=[("transport","Bus kota perlu ditambah sebelum pembatasan kendaraan diberlakukan penuh."),("access","Jangan sampai kebijakan bagus untuk wisatawan malah merugikan pekerja lokal."),("heritage","Pelestarian kawasan bersejarah harus melibatkan warga dan komunitas lokal."),("governance","Pemkot harus membuka data kajian sebelum kebijakan diterapkan."),("economy","Pedagang kecil perlu solusi agar akses pelanggan tetap terjaga."),("transport","Kalau angkutan umum nyaman, warga bisa mempertimbangkan pindah dari kendaraan pribadi."),("access","Trotoar ramah difabel dan lansia harus menjadi prioritas."),("heritage","Kawasan heritage jangan hanya menjadi ruang wisata, warga juga harus bisa hidup di sana."),("governance","Uji coba kebijakan dan evaluasi terbuka akan lebih baik daripada keputusan mendadak."),("economy","Saya mendukung penataan, tetapi biaya distribusi dan parkir jangan memberatkan usaha kecil."),("mixed","Tujuan mengurangi macet baik, namun akses pekerja dan layanan darurat harus dipastikan."),("positive","Jalan lebih aman untuk pejalan kaki bisa meningkatkan kualitas ruang publik."),("negative","Aturan ini belum jelas dan sosialisasinya kurang."),("neutral","Mohon informasi jadwal, zona, dan mekanisme pengecualian kebijakan.")]
NORM={"gak":"tidak","ga":"tidak","nggak":"tidak","enggak":"tidak","gk":"tidak","yg":"yang","dgn":"dengan","krn":"karena","bgt":"banget","aja":"saja","kalo":"kalau"}
STOP={"yang","dan","di","ke","dari","untuk","dengan","ini","itu","ada","akan","saya","kami","kita","mereka","dalam","pada","atau","oleh","sebagai","karena","agar","bisa","dapat","sudah","lebih","juga","saja","nya","sebuah","para"}
NEG={"tidak","bukan","belum","jangan","tanpa"}
LEX={"positive":{"baik","bagus","nyaman","aman","mendukung","setuju","ramah","prioritas","meningkat"},"negative":{"buruk","merugikan","kurang","belum","tidak","jangan","berat","macet","mendadak","masalah","sulit"}}
THEMES={"transportasi_mobilitas":{"angkutan","bus","transportasi","kendaraan","macet","mobilitas","parkir","jalan"},"aksesibilitas":{"akses","difabel","lansia","pekerja","warga","trotoar","layanan","darurat"},"ekonomi_mata_pencaharian":{"pedagang","usaha","ekonomi","biaya","pelanggan","distribusi","kurir"},"heritage_lingkungan":{"heritage","bersejarah","pelestarian","lingkungan","wisata","kawasan"},"tata_kelola_partisipasi":{"pemkot","kebijakan","aturan","kajian","evaluasi","sosialisasi","keputusan","data"}}
def generate(rows=40,seed=20261118):
 rng=random.Random(seed);start=datetime(2026,11,1);out=[]
 for i in range(rows):
  actor,typ=rng.choice(ACTORS);theme,text=TEXTS[i%len(TEXTS)];dt=start+timedelta(days=rng.randrange(14),hours=rng.randrange(24),minutes=rng.randrange(60));target="" if rng.random()<.35 else rng.choice([a for a,_ in ACTORS if a!=actor])
  out.append({"post_id":f"D{i+1:04d}","created_at":dt.isoformat(timespec="seconds"),"author":actor,"actor_type":typ,"text":text,"reply_to":target,"mentions":target if target and rng.random()<.65 else "","likes":rng.randint(0,150),"shares":rng.randint(0,45),"comments":rng.randint(0,60),"platform":rng.choice(["X","Instagram","TikTok"]),"synthetic_theme":theme})
 return out
def preprocess(text):
 s=(text or "").lower();s=re.sub(r"https?://\S+|www\.\S+"," URL ",s);s=re.sub(r"@[\w_]+"," MENTION ",s);s=re.sub(r"#[\w-]+",lambda m:" "+m.group(0)[1:]+" ",s);s=re.sub(r"[^\w\s]"," ",s)
 toks=[NORM.get(t,t) for t in re.sub(r"\s+"," ",s).strip().split()]
 return [t for t in toks if t not in STOP or t in NEG]
def sentiment(text):
 w=(text or "").lower().split();p=sum(x in LEX["positive"] for x in w);n=sum(x in LEX["negative"] for x in w);return "positif" if p>n else "negatif" if n>p else "netral"
def evaluate(gold,pred,labels=("negatif","netral","positif")):
 if len(gold)!=len(pred):raise ValueError("length mismatch")
 cm={g:{p:0 for p in labels} for g in labels}
 for g,p in zip(gold,pred):
  if g not in cm or p not in labels:raise ValueError("invalid label")
  cm[g][p]+=1
 per={}
 for l in labels:
  tp=cm[l][l];fp=sum(cm[g][l] for g in labels if g!=l);fn=sum(cm[l][p] for p in labels if p!=l);pr=tp/(tp+fp) if tp+fp else 0;rc=tp/(tp+fn) if tp+fn else 0
  per[l]={"precision":pr,"recall":rc,"f1":2*pr*rc/(pr+rc) if pr+rc else 0,"support":sum(cm[l].values())}
 n=len(gold);return {"n":n,"accuracy":sum(cm[l][l] for l in labels)/n if n else 0,"macro_f1":sum(v["f1"] for v in per.values())/len(labels),"confusion_matrix":cm,"per_class":per}
def audit(rows):
 headers=list(rows[0]) if rows else [];missing={h:sum(not str(r.get(h,"")).strip() for r in rows) for h in headers};dup=len(rows)-len({tuple(str(r.get(h,"")).strip() for h in headers) for r in rows});dates=[]
 for r in rows:
  try:dates.append(datetime.fromisoformat(r.get("created_at","").replace("Z","+00:00")).date().isoformat())
  except (ValueError,TypeError):pass
 return {"rows":len(rows),"columns":headers,"missing_by_column":missing,"exact_duplicate_rows":dup,"timestamp_profile":{"valid":len(dates),"first_date":min(dates) if dates else None,"last_date":max(dates) if dates else None}}
def themes(rows):
 counts=Counter();examples={k:[] for k in THEMES};freq=Counter()
 for r in rows:
  toks=set(preprocess(r.get("text","")));freq.update(toks)
  for name,terms in THEMES.items():
   hits=sorted(toks&terms)
   if hits:
    counts[name]+=1
    if len(examples[name])<5:examples[name].append({"post_id":r.get("post_id"),"hits":hits,"excerpt":r.get("text","")[:200]})
 return {"method":"keyword dictionary overlap; multi-label exploratory themes, not statistical topic modeling","theme_counts":dict(counts),"top_terms":freq.most_common(20),"evidence_examples":examples}
def network(rows):
 edges=Counter();nodes=set()
 for r in rows:
  a=(r.get("author") or "").strip();b=(r.get("reply_to") or "").strip()
  if a:nodes.add(a)
  if b:nodes.add(b)
  if a and b and a!=b:edges[a,b]+=1
 indeg=Counter();outdeg=Counter()
 for (a,b),w in edges.items():outdeg[a]+=w;indeg[b]+=w
 return {"method":"directed weighted reply graph; author to replied-to account; descriptive only","nodes":len(nodes),"reply_records":sum(edges.values()),"unique_edges":len(edges),"edges":[{"source":a,"target":b,"weight":w} for (a,b),w in sorted(edges.items())],"degree":[{"node":n,"weighted_in":indeg[n],"weighted_out":outdeg[n]} for n in sorted(nodes,key=lambda x:(-indeg[x],-outdeg[x],x))]}
def write_csv(path,rows):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open("w",encoding="utf-8",newline="") as f:w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
def write_theme_svg(counts,path):
 width=900;height=max(150,55+len(counts)*34);left=220;maxv=max(counts.values(),default=1);parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">','<rect width="100%" height="100%" fill="white"/>']
 for i,(name,value) in enumerate(sorted(counts.items(),key=lambda x:-x[1])):
  y=32+i*34;bar=int((width-left-50)*value/maxv);parts.append(f'<text x="{left-10}" y="{y+17}" text-anchor="end" font-family="Arial" font-size="14">{name}</text>');parts.append(f'<rect x="{left}" y="{y}" width="{bar}" height="22" fill="#3567a8"/>');parts.append(f'<text x="{left+bar+6}" y="{y+16}" font-family="Arial" font-size="13">{value}</text>')
 parts.append('</svg>');Path(path).write_text("\n".join(parts),encoding="utf-8")
def run(input_path,outdir,source):
 with input_path.open(encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
 outdir.mkdir(parents=True,exist_ok=True);a=audit(rows);t=themes(rows);n=network(rows)
 for name,obj in (("audit",a),("topics",t),("network",n)):(outdir/f"{name}.json").write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 write_theme_svg(t["theme_counts"],outdir/"theme_chart.svg")
 with (outdir/"annotation_template.csv").open("w",encoding="utf-8",newline="") as f:
  w=csv.writer(f);w.writerow(["post_id","text","annotator_id","gold_label","notes","predicted_label"]);[w.writerow([r.get("post_id"),r.get("text"),"","", "",sentiment(r.get("text"))]) for r in rows]
 rep=["# Social Media Research Report","> Exploratory outputs; human validation required.",f"Data source: {source}","","## Audit",f"- Rows: {a['rows']}",f"- Exact duplicates: {a['exact_duplicate_rows']}","","## Themes","| Theme | Posts |","|---|---:|"]+[f"| {k} | {v} |" for k,v in sorted(t["theme_counts"].items(),key=lambda x:-x[1])]+["","## Evidence"]
 for k,es in t["evidence_examples"].items():
  rep.append(f"### {k}")
  for e in es:rep.append(f"- {e['post_id']}: {e['hits']} — {e['excerpt']}")
 rep += ["","![Theme chart](theme_chart.svg)","","## Reply network",f"- Nodes: {n['nodes']}",f"- Reply records: {n['reply_records']}",f"- Unique edges: {n['unique_edges']}","- Network metrics are descriptive; not proof of influence or coordination.","","## Sentiment","- Lexicon baseline only. Evaluate against human gold labels before calling validated.","","## Limitations","- Themes are keyword dictionary multi-label exploration, not LDA/BERTopic.","- Synthetic data are not evidence about real public opinion.","- Context, negation, slang, sarcasm and regional language may affect results.","- Record source, sampling, filters, timezone, codebook, and versions."]
 (outdir/"report.md").write_text("\n".join(rep)+"\n",encoding="utf-8")
 return {"audit":a,"themes":t,"network":n,"report":outdir/"report.md"}
def main():
 p=argparse.ArgumentParser();sub=p.add_subparsers(dest="cmd",required=True);g=sub.add_parser("generate");g.add_argument("--rows",type=int,default=40);g.add_argument("--seed",type=int,default=20261118);g.add_argument("--output",type=Path,default=Path("data/dummy.csv"));r=sub.add_parser("run");r.add_argument("input",type=Path);r.add_argument("--outdir",type=Path,default=Path("outputs"));r.add_argument("--source",default="unspecified");e=sub.add_parser("evaluate");e.add_argument("annotations",type=Path);e.add_argument("--output",type=Path,default=Path("evaluation.json"));a=p.parse_args()
 if a.cmd=="generate":write_csv(a.output,generate(a.rows,a.seed));print(f"Generated {a.rows}: {a.output}")
 elif a.cmd=="run":res=run(a.input,a.outdir,a.source);print(f"Done rows={res['audit']['rows']} nodes={res['network']['nodes']} out={a.outdir}")
 else:
  with a.annotations.open(encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
  res=evaluate([x["gold_label"] for x in rows],[x["predicted_label"] for x in rows]);a.output.write_text(json.dumps(res,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(a.output)
if __name__=="__main__":main()
