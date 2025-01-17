import {
  pgTable,
  pgEnum,
  varchar,
  integer,
  boolean,
  serial,
  primaryKey,
  index,
} from "drizzle-orm/pg-core";
import { relations, sql } from "drizzle-orm";

export const requestStatusEnum = pgEnum("request_status", [
  "pending",
  "accepted",
]);

export const platforms = pgTable("platforms", {
  id: serial().primaryKey(),
  title: varchar().notNull().unique(),
  urlPattern: varchar("url_pattern").notNull(),
});

export const languages = pgTable("languages", {
  id: serial().primaryKey(),
  title: varchar().notNull().unique(),
});

export const games = pgTable("games", {
  id: serial().primaryKey(),
  title: varchar().notNull().unique(),
  image: varchar().notNull(),
  icon: varchar().notNull(),
});

export const users = pgTable("users", {
  id: serial().primaryKey(),
  nickname: varchar().notNull(),
  email: varchar().unique().notNull(),
  password: varchar(),
  age: integer(),
  profilePic: varchar("profile_pic"),
  isActive: boolean("is_active").default(false).notNull(),
  isSuperuser: boolean("is_superuser").default(false).notNull(),
});

export const usersRelations = relations(users, ({ many }) => ({
  applications: many(applications),
  own_parties: many(parties),
  member_parties: many(partyMembers),
  languages: many(userLanguages),
  platforms: many(userPlatforms),
}));

export const applications = pgTable(
  "applications",
  {
    id: serial().primaryKey(),
    authorId: integer("author_id").references(() => users.id),
    gameId: integer("game_id").references(() => games.id),
    text: varchar().notNull(),
    platformId: integer("platform_id").references(() => platforms.id),
    ranking: varchar(),
  },
  (table) => ({
    searchIndex: index("applications_search_index").using(
      "gin",
      sql`to_tsvector('english', ${table.text})`
    ),
  })
);

export const applicationsRelations = relations(applications, ({ one }) => ({
  author: one(users, {
    fields: [applications.authorId],
    references: [users.id],
  }),
  game: one(games, {
    fields: [applications.gameId],
    references: [games.id],
  }),
  platform: one(platforms, {
    fields: [applications.platformId],
    references: [platforms.id],
  }),
}));

export const parties = pgTable(
  "parties",
  {
    id: serial().primaryKey(),
    leaderId: integer("leader_id").references(() => users.id),
    gameId: integer("game_id").references(() => games.id),
    title: varchar().notNull(),
    description: varchar(),
    minAge: integer("min_range"),
    maxAge: integer("max_range"),
    membersLimit: integer("members_limit"),
    platformId: integer("platform_id").references(() => platforms.id),
  },
  (table) => ({
    searchIndex: index("parties_search_index").using(
      "gin",
      sql`(
        setweight(to_tsvector('english', ${table.title}), 'A') ||
        setweight(to_tsvector('english', ${table.description}), 'B')
    )`
    ),
  })
);

export const partiesRelations = relations(parties, ({ one, many }) => ({
  leader: one(users, {
    fields: [parties.leaderId],
    references: [users.id],
  }),
  platform: one(platforms, {
    fields: [parties.platformId],
    references: [platforms.id],
  }),
  game: one(games, {
    fields: [parties.gameId],
    references: [games.id],
  }),
  members: many(partyMembers),
}));

export const partyMembers = pgTable(
  "party_members",
  {
    userId: integer("user_id")
      .notNull()
      .references(() => users.id),
    partyId: integer("party_id")
      .notNull()
      .references(() => parties.id),
    status: requestStatusEnum("request_status").default("pending").notNull(),
  },
  (t) => ({
    pk: primaryKey({ columns: [t.userId, t.partyId] }),
  })
);

export const partyMembersRelations = relations(partyMembers, ({ one }) => ({
  user: one(users, {
    fields: [partyMembers.userId],
    references: [users.id],
  }),
  party: one(parties, {
    fields: [partyMembers.partyId],
    references: [parties.id],
  }),
}));

export const userLanguages = pgTable(
  "user_languages",
  {
    userId: integer("user_id")
      .notNull()
      .references(() => users.id),
    languageId: integer("language_id")
      .notNull()
      .references(() => languages.id),
  },
  (t) => ({
    pk: primaryKey({ columns: [t.userId, t.languageId] }),
  })
);

export const userLanguagesRelations = relations(userLanguages, ({ one }) => ({
  user: one(users, {
    fields: [userLanguages.userId],
    references: [users.id],
  }),
  language: one(languages, {
    fields: [userLanguages.languageId],
    references: [languages.id],
  }),
}));

export const userPlatforms = pgTable(
  "user_platforms",
  {
    userId: integer("user_id")
      .notNull()
      .references(() => users.id),
    platformId: integer("platform_id")
      .notNull()
      .references(() => platforms.id),
    link: varchar().notNull(),
  },
  (t) => ({
    pk: primaryKey({ columns: [t.userId, t.platformId] }),
  })
);

export const userPlatformsRelations = relations(userPlatforms, ({ one }) => ({
  user: one(users, {
    fields: [userPlatforms.userId],
    references: [users.id],
  }),
  platform: one(platforms, {
    fields: [userPlatforms.platformId],
    references: [platforms.id],
  }),
}));
