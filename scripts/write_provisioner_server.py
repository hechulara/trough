import trough
#from trough.settings import settings

# wsgi entrypoint
def application(env, start_response):
    # TODO: master_mode approach may be wrong below. May want something in `settings`
    try:
        controller = trough.sync.get_controller(server_mode=True)
        controller.check_config()
        segment_name = env.get('wsgi.input').read()
        output = controller.provision_writable_segment(segment_name)
        start_response()
        return output
    except Exception as e:
        start_response('500 Server Error', [('Content-Type', 'text/plain')])
        return [b'500 Server Error: %s' % str(e).encode('utf-8')]