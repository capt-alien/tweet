2018-12-14T05:11:40.017447+00:00 heroku[web.1]: Starting process with command `gunicorn -w 4 app:app`
2018-12-14T05:11:42.813290+00:00 heroku[web.1]: State changed from starting to crashed
2018-12-14T05:11:42.791216+00:00 heroku[web.1]: Process exited with status 1
2018-12-14T05:11:42.691608+00:00 app[web.1]: Traceback (most recent call last):
2018-12-14T05:11:42.691634+00:00 app[web.1]: File "/app/.heroku/python/bin/gunicorn", line 7, in <module>
2018-12-14T05:11:42.691777+00:00 app[web.1]: from gunicorn.app.wsgiapp import run
2018-12-14T05:11:42.691795+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/gunicorn/app/wsgiapp.py", line 9, in <module>
2018-12-14T05:11:42.691932+00:00 app[web.1]: from gunicorn.app.base import Application
2018-12-14T05:11:42.691937+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/gunicorn/app/base.py", line 12, in <module>
2018-12-14T05:11:42.692079+00:00 app[web.1]: from gunicorn import util
2018-12-14T05:11:42.692083+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/gunicorn/util.py", line 12, in <module>
2018-12-14T05:11:42.692256+00:00 app[web.1]: import pkg_resources
2018-12-14T05:11:42.692278+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/pkg_resources/__init__.py", line 77, in <module>
2018-12-14T05:11:42.692455+00:00 app[web.1]: __import__('pkg_resources.extern.packaging.requirements')
2018-12-14T05:11:42.692459+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/pkg_resources/_vendor/packaging/requirements.py", line 9, in <module>
2018-12-14T05:11:42.692601+00:00 app[web.1]: from pkg_resources.extern.pyparsing import stringStart, stringEnd, originalTextFor, ParseException
2018-12-14T05:11:42.692605+00:00 app[web.1]: File "<frozen importlib._bootstrap>", line 983, in _find_and_load
2018-12-14T05:11:42.692794+00:00 app[web.1]: File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
2018-12-14T05:11:42.692917+00:00 app[web.1]: File "<frozen importlib._bootstrap>", line 668, in _load_unlocked
2018-12-14T05:11:42.693049+00:00 app[web.1]: File "<frozen importlib._bootstrap>", line 638, in _load_backward_compatible
2018-12-14T05:11:42.693209+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/pkg_resources/extern/__init__.py", line 43, in load_module
2018-12-14T05:11:42.693357+00:00 app[web.1]: __import__(extant)
2018-12-14T05:11:42.693362+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/pkg_resources/_vendor/pyparsing.py", line 4715, in <module>
2018-12-14T05:11:42.696239+00:00 app[web.1]: _escapedPunc = Word( _bslash, r"\[]-*.$+^?()~ ", exact=2 ).setParseAction(lambda s,l,t:t[0][1])
2018-12-14T05:11:42.696246+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/pkg_resources/_vendor/pyparsing.py", line 1261, in setParseAction
2018-12-14T05:11:42.697114+00:00 app[web.1]: self.parseAction = list(map(_trim_arity, list(fns)))
2018-12-14T05:11:42.697118+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/pkg_resources/_vendor/pyparsing.py", line 1043, in _trim_arity
2018-12-14T05:11:42.697870+00:00 app[web.1]: this_line = extract_stack(limit=2)[-1]
2018-12-14T05:11:42.697874+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/pkg_resources/_vendor/pyparsing.py", line 1027, in extract_stack
2018-12-14T05:11:42.698575+00:00 app[web.1]: frame_summary = traceback.extract_stack(limit=-offset+limit-1)[offset]
2018-12-14T05:11:42.698580+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/traceback.py", line 207, in extract_stack
2018-12-14T05:11:42.698783+00:00 app[web.1]: stack = StackSummary.extract(walk_stack(f), limit=limit)
2018-12-14T05:11:42.698787+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/traceback.py", line 357, in extract
2018-12-14T05:11:42.699068+00:00 app[web.1]: f.line
2018-12-14T05:11:42.699073+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/traceback.py", line 281, in line
2018-12-14T05:11:42.699321+00:00 app[web.1]: self._line = linecache.getline(self.filename, self.lineno).strip()
2018-12-14T05:11:42.699325+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/linecache.py", line 16, in getline
2018-12-14T05:11:42.699462+00:00 app[web.1]: lines = getlines(filename, module_globals)
2018-12-14T05:11:42.699466+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/linecache.py", line 47, in getlines
2018-12-14T05:11:42.699616+00:00 app[web.1]: return updatecache(filename, module_globals)
2018-12-14T05:11:42.699621+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/linecache.py", line 136, in updatecache
2018-12-14T05:11:42.699799+00:00 app[web.1]: with tokenize.open(fullname) as fp:
2018-12-14T05:11:42.699839+00:00 app[web.1]: AttributeError: module 'tokenize' has no attribute 'open'
