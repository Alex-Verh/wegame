CREATE TYPE "public"."request_status" AS ENUM('pending', 'accepted');--> statement-breakpoint
ALTER TABLE "party_members" ADD COLUMN "request_status" "request_status" DEFAULT 'pending' NOT NULL;