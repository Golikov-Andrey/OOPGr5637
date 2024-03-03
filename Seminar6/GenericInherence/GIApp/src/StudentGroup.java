

import java.util.Iterator;
import java.util.List;

//T - string
//V - int
public class StudentGroup<T extends Comparable<T>,V> implements Iterable<Student<T,V>> {
    private List<Student<T,V>> group;
    private V idGroup;

    public StudentGroup(List<Student<T,V>> group, V idGroup) {
        this.group = group;
        this.idGroup = idGroup;
    }

    public List<Student<T,V>> getGroup() {
        return group;
    }

    public void setGroup(List<Student<T,V>> group) {
        this.group = group;
    }

    public V getIdGroup() {
        return idGroup;
    }

    public void setIdGroup(V idGroup) {
        this.idGroup = idGroup;
    }

     @Override
    public String toString() {
        return "StudentGroup{" +
                "group=" + group +
                ", idGroup=" + idGroup +
                '}';
    }

    // @Override
    // public Iterator<Student> iterator() {
    //    return new Iterator<Student>() {

    //     private int counter;

    //     @Override
    //     public boolean hasNext() {

    //         if(counter<group.size())
    //         {
    //             return true;
    //         }
    //         else
    //         {
    //             return false;
    //         }            
    //     }

    //     @Override
    //     public Student next() {            
    //         return group.get(counter++);
    //     }
        
    //    };
        
    // }

     @Override
    public Iterator<Student<T,V>> iterator() {
       return new StudentIterator<T,V>(group);
        
    }
    
    
}
