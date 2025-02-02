ALTER TABLE "applications" ALTER COLUMN "author_id" SET NOT NULL;--> statement-breakpoint
ALTER TABLE "applications" ALTER COLUMN "game_id" SET NOT NULL;--> statement-breakpoint
ALTER TABLE "applications" ALTER COLUMN "platform_id" SET NOT NULL;--> statement-breakpoint
ALTER TABLE "parties" ALTER COLUMN "leader_id" SET NOT NULL;--> statement-breakpoint
ALTER TABLE "parties" ALTER COLUMN "game_id" SET NOT NULL;--> statement-breakpoint
ALTER TABLE "parties" ALTER COLUMN "min_range" SET DEFAULT 0;--> statement-breakpoint
ALTER TABLE "parties" ALTER COLUMN "min_range" SET NOT NULL;--> statement-breakpoint
ALTER TABLE "parties" ALTER COLUMN "max_range" SET DEFAULT 100;--> statement-breakpoint
ALTER TABLE "parties" ALTER COLUMN "max_range" SET NOT NULL;--> statement-breakpoint
ALTER TABLE "parties" ALTER COLUMN "members_limit" SET DEFAULT 100;--> statement-breakpoint
ALTER TABLE "parties" ALTER COLUMN "members_limit" SET NOT NULL;--> statement-breakpoint
ALTER TABLE "parties" ALTER COLUMN "platform_id" SET NOT NULL;