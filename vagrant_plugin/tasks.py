import vagrant
import os
from jinja2 import Environment, FileSystemLoader
from cloudify import ctx
from cloudify.decorators import operation

VAGRANTFILE_TEMPLATE = 'Vagrantfile.template'
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


@operation
def start(vbox_url, **kwargs):
    env = Environment(loader=FileSystemLoader(CURRENT_DIR))
    template = env.get_template(VAGRANTFILE_TEMPLATE)

    vm = {'vbox_name': kwargs['vbox_name'],
            'vbox_url': vbox_url,
            'vm_name': kwargs['vm_name'],
            'vm_cpus': kwargs['vm_cpus'],
            'vm_memory': kwargs['vm_memory']}
    with open('Vagrantfile', 'w') as f:
        f.write(template.render(vm=vm))

    v = vagrant.Vagrant()
    v.up()
