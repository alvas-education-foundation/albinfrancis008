/* Program to convert a char array to a string in Java*/
class CharArrayToString
{
public static void main(String args[])
{
char[] ch = {'g', 'o', 'o', 'd', ' ', 'm', 'o', 'r', 'n', 'i', 'n', 'g'};
String str = new String(ch);
System.out.println(str);
String str2 = String.valueOf(ch);
System.out.println(str2);
}
}
