package Domain;

public class Employee extends WorkingPerson{
    private String special;

    public Employee(String firstName, int age, String special) {
        super(firstName, age);
        this.special = special;
    }
}
