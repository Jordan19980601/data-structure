struct Role {
 char *name;
 int level; 
 int hp; 
 int ap; 
 int dp; 
 int sp; 
};
void dump_role(Role& role) {
 cout << " �W�١G " << role.name << endl;
 cout << " ���šG " << role.level << endl;
 cout << " �ͩR��G " << role.name << endl;
 cout << " �����O�G " << role.name << endl;
 cout << " ���m�O�G " << role.dp << endl;
 cout << " �믫��q�G " << role.name << endl;
 }
void test_role() {
char name[] = " ���H��";

struct Role role;
 role.name = name;
 role.level = 1;
 role.hp = 10;
 role.ap = 1;
 role.dp = 1;
 role.sp = 2;

 dump_role(role);
 }
 test role;
