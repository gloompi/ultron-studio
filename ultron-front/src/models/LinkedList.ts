class LinkedList<T> {
  private _value?: T;
  private _next?: LinkedList<T>;
  private _prev?: LinkedList<T>;
  private _length: number = 0;

  constructor(value?: T, next?: LinkedList<T>, prev?: LinkedList<T>) {
    this._value = value;
    this._next = next;
    this._prev = prev;
  }

  public makeList = (list: T[]): LinkedList<T> => {
    this.value = list[0];
    this.next = new LinkedList(list[1]);
    this.length = 1;

    let tmp = this.next;

    for (let i = 1; i < list.length; i++) {
      tmp.value = list[i];

      if (list[i++]) {
        tmp.next = new LinkedList(list[i++]);
        tmp = tmp.next;
      }

      this.length++;
    }

    return this;
  };

  get value(): T | undefined {
    return this._value;
  }

  get next(): LinkedList<T> | undefined {
    return this._next;
  }

  get prev(): LinkedList<T> | undefined {
    return this._prev;
  }

  get length(): number {
    return this._length;
  }

  set value(value: T | undefined) {
    this._value = value;
  }

  set next(next: LinkedList<T> | undefined) {
    this._next = next;
  }

  set prev(prev: LinkedList<T> | undefined) {
    this._prev = prev;
  }

  set length(value: number) {
    this._length = value;
  }
}

export function findInList<T>(
  linkedList: LinkedList<T>,
  value: T
): LinkedList<T> | false {
  if (linkedList.value === value) {
    return linkedList;
  }

  let tmp = linkedList.next;

  while (tmp) {
    if (tmp.value === value) {
      return tmp;
    }

    tmp = tmp.next;
  }

  return false;
}

export default LinkedList;
