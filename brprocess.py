#!/usr/bin/python

import vymgmt

def set_vlan(ethernet,vlan,desc,ip):
	vyos = vymgmt.Router('13.231.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.set("int eth %s vif %s desc %s " %(ethernet,vlan,desc))
        vyos.set("int eth %s vif %s address %s" %(ethernet,vlan,ip))
        vyos.commit()
        vyos.save()
        vyos.exit()

def get_vlan():
	vyos = vymgmt.Router('13.231.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vlan = vyos.run_op_mode_command("sh int eth")
        vyos.logout()
        return vlan

def del_vlan(ethernet,vlan):
	vyos = vymgmt.Router('13.231.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.delete("int eth %s vif %s" %(ethernet,vlan))
        vyos.commit()
        vyos.save()
        vyos.exit()

def set_bridge(bridge, ethernet, ip):
	vyos = vymgmt.Router('13.231.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.set("int bridge %s" %(bridge))
	vyos.set("int bridge %s address %s" %(bridge,ip))
        vyos.set("int bridge %s stp true" %(bridge))
	vyos.commit()
        vyos.save()
        vyos.exit()

def get_bridge():
	vyos = vymgmt.Router('13.231.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        br = vyos.run_op_mode_command("sh int bridge")
        vyos.logout()
        return br

def del_bridge(bridge):
	vyos = vymgmt.Router('13.231.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.delete("int bridge %s" %(bridge))
        vyos.commit()
        vyos.save()
        vyos.exit()

if __name__ == '__main__':
        app.run(debug=True)
