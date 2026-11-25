const fs=require('fs'),vm=require('vm'),assert=require('assert');
const base=__dirname+'/../';
const sandbox={window:{},console,Date,Math};vm.createContext(sandbox);
for(const f of ['data/catalog.js','data/practice.js'])vm.runInContext(fs.readFileSync(base+f,'utf8'),sandbox,{filename:f});
const C=sandbox.window.TESERACTO_CATALOG,P=sandbox.window.TE_PRACTICE;
assert.equal(C.modules.length,27);
const ids=new Set(C.modules.map(m=>m.id));assert.equal(ids.size,C.modules.length);
let cases=0;
for(const m of C.modules){
 assert(m.title&&m.summary&&m.examples.length>=2,m.id);
 for(const d of m.strong)assert(ids.has(d),`${m.id} tiene prerequisito inexistente ${d}`);
 for(const mode of ['guided','independent','transfer'])for(let i=1;i<=300;i++){
  const q=P.generate(m.id,i,mode);assert(q.prompt.length>10&&q.work.length>8,`ejercicio incompleto ${m.id}`);
  assert(P.correct(q,q.answer),`no acepta su propia solución ${m.id} ${mode} ${i}: ${q.answer} / ${q.prompt}`);
  if(q.kind==='fraction')assert(P.correct(q,String(P.parseNum(q.answer)).replace('.',',')),`decimal incorrecto ${m.id}`);
  cases++;
 }
}
assert(P.correct({kind:'fraction',answer:'1/2'},'2/4'));
assert(P.correct({kind:'number',answer:'0.75'},'0,75'));
assert(!P.correct({kind:'number',answer:'10'},'11'));
console.log('OK:',C.modules.length,'temas,',cases,'ejercicios generados y verificados');
