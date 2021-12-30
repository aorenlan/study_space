# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
def readXML():
	domTree = parse("./customer.xml")
	# 文档根元素
	rootNode = domTree.documentElement
	print(rootNode.nodeName)

	# 所有顾客
	customers = rootNode.getElementsByTagName("customer")
	print("****所有顾客信息****")
	for customer in customers:
		if customer.hasAttribute("ID"):
			print("ID:", customer.getAttribute("ID"))
			# name 元素
			name = customer.getElementsByTagName("name")[0]
			print(name.nodeName, ":", name.childNodes[0].data)
			# phone 元素
			phone = customer.getElementsByTagName("phone")[0]
			print(phone.nodeName, ":", phone.childNodes[0].data)
			# comments 元素
			comments = customer.getElementsByTagName("comments")[0]
			print(comments.nodeName, ":", comments.childNodes[0].data)

def writeXML():
	domTree = parse("./customer.xml")
	# 文档根元素
	rootNode = domTree.documentElement

	# 新建一个customer节点
	customer_node = domTree.createElement("customer")
	customer_node.setAttribute("ID", "C003")

	# 创建name节点,并设置textValue
	name_node = domTree.createElement("name")
	name_text_value = domTree.createTextNode("kavin")
	name_node.appendChild(name_text_value)  # 把文本节点挂到name_node节点
	customer_node.appendChild(name_node)

	# 创建phone节点,并设置textValue
	phone_node = domTree.createElement("phone")
	phone_text_value = domTree.createTextNode("32467")
	phone_node.appendChild(phone_text_value)  # 把文本节点挂到name_node节点
	customer_node.appendChild(phone_node)

	# 创建comments节点,这里是CDATA
	comments_node = domTree.createElement("comments")
	cdata_text_value = domTree.createCDATASection("A small but healthy company.")
	comments_node.appendChild(cdata_text_value)
	customer_node.appendChild(comments_node)

	rootNode.appendChild(customer_node)

	with open('added_customer.xml', 'w') as f:
		# 缩进 - 换行 - 编码
		domTree.writexml(f, addindent='  ', encoding='utf-8')

if __name__ == '__main__':
	writeXML()
