class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.count = 0;
  }



printAll() {
  let currentNode = this.head;
  let text = "[";

  while (currentNode != null) {
    text += currentNode.data;

    currentNode = currentNode.next;

    // 다음 노드가 null이 아니면 → 즉 아직 끝이 아니면 쉼표 찍기
    if (currentNode != null) {
      text += ", ";
    }
  }

  text += "]";
  console.log(text);
}

clear(){
    this.head = null;
    this.count = 0;
}



  //인덱스에 원하는 값 넣기
  insertAT(index, data) {
    if (index > this.count || index < 0) {
      throw new Error("Index out of bounds");
    }

    let newNode = new Node(data);

    if (index == 0) {
      newNode.next = this.head;
      this.head = newNode;
    } else {
      let currentNode = this.head;
      for (let i = 0; i < index - 1; i++) {
        currentNode = currentNode.next;
      }
      newNode.next = currentNode.next;
      currentNode.next = newNode;
    }

    this.count++;
  }


  insertLast(data){
    this.insertAT(this.count , data);
  }

  deletAt(index) {
    if (index > this.count || index < 0) {
        throw new Error("Index out of bounds");
    }

    let currentNode = this.head;

    if(index == 0){
        let deletedNode = this.head;
        this.head = this.head.next;
        this.count--;
        return deletedNode;

    }else{
        for(let i = 0; i < index-1; i++){
            currentNode = currentNode.next;
    
        }
        let deletedNode = currentNode.next;
        currentNode.next = currentNode.next.next;
        this.count--;
        return deletedNode;

    }

  }
    deletLast(){
        return this.deletAt(this.count - 1);
    }

    getNodeAt(index){
       if(index >= this.count || index < 0){
            throw new Error("Index out of bounds");
        }

        let currentNode = this.head;
        for(let i = 0; i < index; i++){
            currentNode = currentNode.next;
        }

        return currentNode;
       } 
    }
  


export { Node, LinkedList };
