#!/usr/bin/env python3
"""Smoke-test navegación y ejercicios en navegador real (opcional)."""
from pathlib import Path
import re,base64
from subprocess import Popen,DEVNULL
from playwright.sync_api import sync_playwright
import time
R=Path(__file__).resolve().parents[1]; PORT=8765
s=Popen(['python','-m','http.server',str(PORT),'--directory',str(R)],stdout=DEVNULL,stderr=DEVNULL)
try:
 with sync_playwright() as pw:
  browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  for kind,viewport in [('desktop',{'width':1440,'height':900}),('mobile',{'width':390,'height':844})]:
   page=browser.new_page(viewport=viewport,device_scale_factor=1)
   errors=[]
   page.on('pageerror',lambda e:errors.append(str(e)))
   html=(R/'index.html').read_text()
   html=re.sub(r'<script[^>]*src="[^"]+"[^>]*></script>','',html)
   html=re.sub(r'<link[^>]*href="\./assets/styles.css"[^>]*>','',html)
   logo=base64.b64encode((R/'assets/logo-teseracto.svg').read_bytes()).decode()
   html=html.replace('./assets/logo-teseracto.svg','data:image/svg+xml;base64,'+logo)
   page.set_content(html,wait_until='domcontentloaded')
   page.add_style_tag(content=(R/'assets/styles.css').read_text())
   for filename in ['data/catalog.js','data/practice.js','assets/app.js']:page.add_script_tag(content=(R/filename).read_text())
   page.locator('h1').first.wait_for()
   assert 'matemáticas' in page.locator('h1').first.inner_text().lower(),page.locator('h1').first.inner_text()
   page.screenshot(path=str(R.parent/f'teseracto-matematicas-{kind}.png'),full_page=True)
   page.evaluate("location.hash='/catalogo?etapa=primaria'")
   assert page.get_by_text('Fracciones equivalentes').count()>0
   page.locator('#find-topic').fill('parábolas')
   assert 'temas' in page.locator('#catalog-results').inner_text().lower()
   page.evaluate("location.hash='/tema/fracciones-equivalentes'")
   page.locator('h1').first.wait_for()
   assert 'Fracciones equivalentes' in page.locator('h1').first.inner_text()
   assert page.locator('#svgwrap svg').count()==1
   page.get_by_role('button',name='01 · Con apoyo').click()
   assert page.locator('#quiz-answer').count()==1
   # get correct answer from generated session by pulling node dynamic data? not available; use dummy answer
   page.locator('#quiz-answer').fill('8')
   page.get_by_role('button',name='Comprobar respuesta').click()
   assert page.get_by_role('button',name='Siguiente ejercicio →').count()==1
   page.get_by_role('button',name='Siguiente ejercicio →').click()
   assert page.locator('#quiz-answer').count()==1
   page.evaluate("location.hash='/maer'")
   page.get_by_role('button',name='Empezar exploración').click()
   assert page.locator('#diag-answer').count()==1
   page.evaluate("location.hash='/progreso'")
   assert page.get_by_role('button',name='Exportar progreso JSON').count()==1
   assert not errors,(kind,errors)
   page.close()
   print(kind,'OK')
  browser.close()
finally:
 s.terminate();s.wait()
