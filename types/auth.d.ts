declare module "#auth-utils" {
  interface User {
    id: number;
    nickname: string;
    email: string;
    age: number | null;
    profilePic: string | null;
    isActive: boolean;
    isSuperuser: boolean;
  }
}
export {};
