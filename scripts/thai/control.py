#!/usr/bin/env python3
"""Small JSON-lines client for an explicitly launched isolated VectorCraft test app."""
import json,socket,sys
PORT=17973
def request(method,params=None):
 with socket.create_connection(('127.0.0.1',PORT),timeout=75) as s:
  s.settimeout(75)
  s.sendall((json.dumps({'id':1,'method':method,'params':params or {}},ensure_ascii=False)+'\n').encode())
  with s.makefile('rb') as f:response=json.loads(f.readline())
 if not response.get('ok'):raise RuntimeError(response.get('error',response))
 return response.get('result')
def command(command_id,**params):return request('engine.execute',{'command':command_id,'params':params})
if __name__=='__main__':print(json.dumps(request(sys.argv[1],json.loads(sys.argv[2]) if len(sys.argv)>2 else {}),ensure_ascii=False,indent=2))
