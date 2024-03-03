

//T - string
//V - int
public class Student<T extends Comparable<T>,V> extends Person<T,V> implements Comparable<Student<T,V>> {

    private V id;
   // private static int generalId;

    public Student(T name, V age, V id) {
        super(name, age);
        this.id = id;
        //this.id = generalId;
       // generalId++;
    }


    public V getId() {
        return id;
    }


    @Override
    public String toString() {
        return "Students [age=" + super.getAge() + ", name=" + super.getName() + ", id=" + id + "]";
    }

    @Override
    public int compareTo(Student<T,V> o) {

        return super.getName().compareTo(o.getName());

        // System.out.println(super.getName()+" - "+o.getName());
        // if(super.getAge()==o.getAge())
        // {
        //     id.
        //     if(id==o.id)return 0 ;
        //     if(id>o.id)return 1;
        //     else return -1;
        //     //return 0;
        // }

        // if(super.getAge()>o.getAge())
        // return 1;
        // else
        // return -1;        
    }


    
    
    
}


