/*
export interface ApplicationT {
  id: number;
  authorId?: number | null;
  gameId?: number | null;
  text: string;
  platformId?: number | null;
  ranking: string | null;
  author?: UserT | null;
  game?: GameT | null;
  platform?: PlatformT | null;
}

export interface PartyT {
  id: number;
  leaderId?: number | null;
  gameId?: number | null;
  title: string;
  description: string | null;
  minAge: number | null;
  maxAge: number | null;
  membersLimit: number | null;
  platformId?: number | null;
  leader?: UserT | null;
  game?: GameT | null;
  platform?: PlatformT | null;
  members?: Array<{ userId: number; status: string }> | null;
}

export interface UserT {
  id: number;
  age: number | null;
  nickname: string;
  email?: string | null;
  profilePic: string | null;
  languages?: Array<{ languageId: number; language?: LanguageT }> | null;
  platforms?: Array<{
    platformId: number;
    link: string;
    platform?: PlatformT;
  }> | null;
  applications?: Array<ApplicationT> | null;
  parties?: Array<PartyT> | null;
  ownParties?: Array<PartyT> | null;
}
*/
