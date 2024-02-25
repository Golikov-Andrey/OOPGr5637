package Model.Domain;

/**
 * Класс Student
 * Представляет собой структуру для создания объектов типа "Student" с идентификатором студентов и генератором id
 */
public class Student extends Person implements Comparable<Student> {
    private int id;
    private static int idGenerator;

    public Student(String name, int age) {
        super(name, age);
        idGenerator++;
        this.id = idGenerator;
    }

    public int getId() {
        return id;
    }

    @Override
    public String toString() {
        return "Student{" +
                "id=" + id + " name " + super.getName() + " age " + super.getAge() +
                '}';
    }

    /**
     * @apiNote Метод для сравнения студентов по возрасту и по id
     * @param o the object to be compared.
     * @return возвращает:
     * 0, если значения равны;
     * -1, если вызываемый объект меньше o;
     * +1, если вызываемый объект больше o.
     */
    @Override
    public int compareTo(Student o) {
        System.out.println(this.getName() + " - " + o.getName());
        if (this.getAge() > o.getAge()) return 1;
        if (this.getAge() < o.getAge()) return -1;
        if (this.getId() > o.getId()) return 1;
        if (this.getId() < o.getId()) return -1;
        return 0;
    }
}
