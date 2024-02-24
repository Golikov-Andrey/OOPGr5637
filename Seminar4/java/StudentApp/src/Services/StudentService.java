package Services;

import java.util.ArrayList;
import java.util.List;

import Domain.Employee;
import Domain.PersonComparator;
import Domain.Student;

public class StudentService implements iPersonService<Student>  {

    private int count;
    private List<Student> students;

    public StudentService() {
        this.students = new ArrayList<>();
    }

    @Override
    public List<Student> getAll() {
       return students;
    }

    @Override
    public void create(String name, int age) {
       Student stud = new Student(name, age);
       count++;
       students.add(stud);
    }   
    
    public void sortByFIO()
    {
        PersonComparator<Student> persComp = new PersonComparator<Student>();
        students.sort(persComp);
    }
}
