

import java.util.Iterator;
import java.util.List;

//T - string
//V - int
public class StudentIterator<T extends Comparable<T>,V> implements Iterator<Student<T,V>> {
    private int counter;
    private final List<Student<T,V>> students;
    
    public StudentIterator(List<Student<T,V>> students) {
        this.students = students;
        this.counter = 0;
    }
    
    @Override
    public boolean hasNext() {
       return counter<students.size();
    }
    @Override
    public Student<T,V> next() {
        if(!hasNext())
        {
            return null;
        }
        //counter++;
        return students.get(counter++);        
    }
    
}

