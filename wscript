## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    module = bld.create_ns3_module('cosem', ['applications', 'internet'])
    module.source = [
        'model/cosem-al-server.cc',
        'model/cosem-ap-server.cc',
        'model/cosem-al-client.cc',
        'model/cosem-ap-client.cc',
        'model/udp-cosem-client.cc',
        'model/udp-cosem-server.cc',
        'model/cosem-header.cc',
        'model/dc-app.cc',
        'model/dr-app.cc',
        'model/dr-header.cc',
        'model/mdm-app.cc',
        'helper/udp-cosem-client-helper.cc',
        'helper/udp-cosem-server-helper.cc',
        'helper/data-concentrator-helper.cc',
        'helper/demand-response-application-helper.cc',
        'helper/mdm-application-helper.cc',
        ]

   ## module_test = bld.create_ns3_module_test_library('cosem')
   ## module_test.source = [
   ##     'test/udp-client-server-test.cc',
   ##     ]

    headers = bld.new_task_gen(features=['ns3header'])
    headers.module = 'cosem'
    headers.source = [
        'model/cosem-al-server.h',
        'model/cosem-ap-server.h',
        'model/cosem-al-client.h',
        'model/cosem-ap-client.h',
        'model/udp-cosem-client.h',
        'model/udp-cosem-server.h',
        'model/cosem-header.h',
        'model/dr-header.h',
        'model/dc-app.h',
        'model/dr-app.h',
        'model/mdm-app.h',
        'helper/udp-cosem-client-helper.h',
        'helper/udp-cosem-server-helper.h',
        'helper/data-concentrator-helper.h',
        'helper/demand-response-application-helper.h',
        'helper/mdm-application-helper.h',
        ]

   # bld.ns3_python_bindings()
