import { Node , LinkedList } from "./LinkedList.mjs";

let node1 = new Node(10);
let node2 = new Node(20);
let node3 = new Node(30);


node1.next = node2;
node2.next = node3;

console.log(node1.data); 
console.log(node1.next.data); 
console.log(node1.next.next.data); 


let list = new LinkedList();
console.log("=========insertAT()=========");
list.insertAT(0,0);
list.insertAT(1,1);
list.insertAT(2,2);
list.insertAT(3,3);
list.insertAT(4,4);
list.printAll();


console.log("=========clear()=========");
list.clear();
list.printAll();


console.log("=========insertLast()=========");
list.insertLast(0);
list.insertLast(1);
list.insertLast(2);
list.printAll();

console.log("=========deleteAt()=========");
list.deletAt(0);
list.printAll();
list.deletAt(1);
list.printAll();


console.log("=========deleteLast()=========");
list.insertLast(5);
list.printAll();
list.deletLast();
list.printAll();


console.log("=========getNode()=========");
list.insertLast(1);
list.insertLast(2);
list.insertLast(3); 
list.insertLast(4);
list.insertLast(5); 


list.printAll();
let secoundNode = list.getNodeAt(2); 
console.log(secoundNode.data); 