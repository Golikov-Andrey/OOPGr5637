import java.util.ArrayList;
import java.util.List;

import Controller.ControllerClass;
import Controller.Interfaces.iGetModel;
import Controller.Interfaces.iGetView;
import Model.FileModelClass;
import Model.ModelClass;
import Model.Domain.Student;
import View.ViewClass;

public class App {
    public static void main(String[] args) throws Exception {
       
        Student student1 = new Student("Ivan", 21);
        Student student2 = new Student("Anna", 25);
        Student student3 = new Student("Vasya", 22);
        Student student4 = new Student("Nastya", 27);
        Student student5 = new Student("Vasilisa", 26);
        Student student6 = new Student("Karina", 25);
        Student student7 = new Student("Andrey", 22);
        Student student8 = new Student("Masha", 27);
        Student student9 = new Student("Irina", 28);
        Student student10 = new Student("Nikolay", 30);

        List<Student> studList = new ArrayList<>();
        studList.add(student1);
        studList.add(student2);
        studList.add(student3);
        studList.add(student4);
        studList.add(student5);
        studList.add(student6);
        studList.add(student7);
        studList.add(student8);
        studList.add(student9);
        studList.add(student10);

        FileModelClass fmClass = new FileModelClass("StudentDB.csv");
        //fmClass.saveAllStudentToFile(studList);

        iGetView view = new ViewClass();
        //iGetModel model = new ModelClass(studList);

        ControllerClass controller = new ControllerClass(fmClass, view);

        //controller.update();
        controller.run();

    }
}
