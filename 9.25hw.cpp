struct Role {
 char *name;
 int level; 
 int hp; 
 int ap; 
 int dp; 
 int sp; 
};
void dump_role(Role& role) {
 cout << " 名稱： " << role.name << endl;
 cout << " 等級： " << role.level << endl;
 cout << " 生命質： " << role.name << endl;
 cout << " 攻擊力： " << role.name << endl;
 cout << " 防禦力： " << role.dp << endl;
 cout << " 精神能量： " << role.name << endl;
 }
void test_role() {
char name[] = " 路人甲";

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
