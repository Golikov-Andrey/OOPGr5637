package Model;

import java.util.List;

import Controller.Interfaces.iGetModel;
import Model.Domain.Student;

public class ModelClass implements iGetModel {
    
    private List<Student> students;

    public ModelClass(List<Student> students) {
        this.students = students;
    }

    public List<Student> getAllStudents() {
        return students;
    }  
}
