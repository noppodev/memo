
import os
path = r'C:\Users\orgra\Downloads\noppomemo\dist\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

meta = '''
    <!-- PWA Settings -->
    <link rel='manifest' href='manifest.webmanifest'>
    <meta name='theme-color' content='#F2F2F7'>
    <link rel='apple-touch-icon' href='icon-512.png'>
    <!-- /PWA Settings -->'''

sw_script = '''
    <!-- Service Worker Registration -->
    <script>
      if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
          navigator.serviceWorker.register('sw.js');
        });
      }
    </script>
    <!-- /Service Worker Registration -->'''

if 'manifest.webmanifest' not in content:
    content = content.replace('<head>', '<head>' + meta)

if 'sw.js' not in content:
    content = content.replace('</body>', sw_script + '</body>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

