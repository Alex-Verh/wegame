export interface User {
    id: number;
    nickname: string;
    email: string;
    profilePic: string;
    languages: Array<{ languageId: number }>;
    platforms: Array<{ platformId: number, link: string }>
    applications: Array<any>,
    parties: Array<any>
    ownParties: Array<any> 
  }