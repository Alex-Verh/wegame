import * as schema from "~/server/database/schema";
import { drizzle } from "drizzle-orm/node-postgres";
export { eq, and, or, sql, desc, asc } from "drizzle-orm";
export const tables = schema;
const db = drizzle(useRuntimeConfig().databaseUrl, {
  schema,
  logger: true,
});
export function useDrizzle() {
  return db;
}
