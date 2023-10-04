from user import User
from pyvis.network import Network

user_id = None # Put user_id you need here
user = User(user_id)
data = user.get_user_friends(user_id)

ids = data['items']

net = Network()

nodes = []
edges = []

nodes.append(user_id)
nodes.extend(ids)

for uid in ids:
    edges.append((user_id, uid))
    user_friends = User.get_user_friends(uid)['items']
    result = list(set(user_friends) & set(ids))
    for common in result:
        edges.append((common, uid))


label = [user_id]
label.extend([*ids])
label = [str(x) for x in label]
print(label)
net.add_nodes(
    nodes=nodes,
    label=label
)

net.add_edges(edges=edges)

net.show('graph.html', notebook=False)  # save visualization in 'graph.html'
