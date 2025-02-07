import * as schema from "~/server/database/schema";
import { drizzle } from "drizzle-orm/node-postgres";

export { eq, and, or, sql, desc, asc } from "drizzle-orm";

export const tables = schema;

const db = drizzle(useRuntimeConfig().databaseUrl, {
  schema,
  logger: true,
});

export function useDB() {
  return db;
}

export type Game = typeof tables.games.$inferSelect;
export type Platform = typeof tables.platforms.$inferSelect;
export type Language = typeof tables.languages.$inferSelect;
export type Application = typeof tables.applications.$inferSelect & {
  game: Game;
  platform: Platform;
};
export type Party = typeof tables.parties.$inferSelect & {
  game: Game;
  platform: Platform;
  members: { userId: number; status: "pending" | "accepted" }[];
};
export type User = Omit<typeof tables.users.$inferSelect, "password"> & {
  platforms: { platform: Platform; link: string }[];
  languages: Language[];
};
