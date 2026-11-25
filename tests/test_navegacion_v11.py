from pathlib import Path
import re,base64
from subprocess import Popen, DEVNULL
from playwright.sync_api import sync_playwright
from urllib.request import urlopen
import time
R=Path(__file__).resolve().parents[1]; PORT=8769
server=Popen(['python','-m','http.server',str(PORT),'--directory',str(R)],stdout=DEVNULL,stderr=DEVNULL)
try:
 for _ in range(30):
  try: urlopen(f'http://127.0.0.1:{PORT}/',timeout=1);break
  except OSError: time.sleep(.1)
 with sync_playwright() as pw:
  b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  for name,w,h in [('desktop',1440,900),('tablet',768,1024),('mobile',390,844)]:
   page=b.new_page(viewport={'width':w,'height':h});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   html=(R/'index.html').read_text();html=re.sub(r'<script[^>]*src="[^"]+"[^>]*></script>','',html);html=re.sub(r'<link[^>]*href="\./assets/styles.css"[^>]*>','',html);html=html.replace('./assets/logo-teseracto.svg','data:image/svg+xml;base64,'+base64.b64encode((R/'assets/logo-teseracto.svg').read_bytes()).decode());page.set_content(html);page.add_style_tag(content=(R/'assets/styles.css').read_text());[page.add_script_tag(content=(R/x).read_text()) for x in ['data/catalog.js','data/practice.js','assets/app.js']];page.get_by_role('heading',name='¿En qué curso estás?').wait_for()
   page.get_by_role('link',name='6.º Primaria',exact=False).first.click()
   page.locator('#catalog-results h2').wait_for();assert page.locator('#catalog-results h2').inner_text()=='6.º Primaria'
   assert page.locator('.module-card').count()==16, page.locator('.module-card').count()
   assert page.locator('.catalog-block').count()>=3
   page.locator('#find-topic').fill('fracciones');assert page.locator('.module-card').count()>=5
   page.locator('#find-topic').fill('parabolas');assert page.locator('.module-card').count()==0
   page.get_by_role('button',name='Buscar en todos los cursos').click();assert page.locator('.legacy-card').count()==1
   assert page.locator('.legacy-card a').get_attribute('href')=='./temas/funciones/parabolas.html'
   page.locator('#find-topic').fill('vertice');assert page.locator('.module-card').count()>=2
   page.locator('#find-topic').fill('');page.locator('#grade-filter').select_option('2B');assert page.locator('#catalog-results h2').inner_text()=='2.º Bachillerato'
   page.locator('#group-filter').select_option('Funciones y gráficas');assert page.locator('.module-card').count()==5
   page.screenshot(path=str(R.parent/f'teseracto-v11-{name}.png'),full_page=True)
   page.get_by_role('link',name='Parábolas: de cero al vértice').click();page.locator('.legacy-banner a').wait_for();assert page.locator('.legacy-banner a').count()==1
   page.get_by_role('button',name='01 · Con apoyo').click();page.locator('#quiz-answer').fill('2');page.get_by_role('button',name='Comprobar respuesta').click();assert page.get_by_role('button',name='Siguiente ejercicio →').count()==1
   page.evaluate("location.hash='/catalogo?curso=6P'");page.locator('#catalog-results h2').wait_for();assert page.locator('#catalog-results h2').inner_text()=='6.º Primaria'
   page.get_by_role('link',name='Fracciones equivalentes',exact=True).click();page.locator('.legacy-banner a').wait_for();assert page.locator('.legacy-banner a').get_attribute('href').endswith('01_Cuaderno_Fracciones_Alumno.pdf')
   assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+1'),name
   assert not errors,(name,errors);print(name,'OK');page.close()
  b.close()
finally:
 server.terminate();server.wait()
