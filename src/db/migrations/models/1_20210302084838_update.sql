-- upgrade --
CREATE TABLE IF NOT EXISTS "blogcategory" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "published" BOOL NOT NULL  DEFAULT True,
    "description" TEXT NOT NULL,
    "parent_id" INT REFERENCES "blogcategory" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "blogcategory" IS 'Class category ';;
CREATE TABLE IF NOT EXISTS "post" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(500) NOT NULL,
    "mini_text" TEXT NOT NULL,
    "text" TEXT NOT NULL,
    "create_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "publish_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "image" VARCHAR(500),
    "published" BOOL NOT NULL  DEFAULT True,
    "viewed" INT NOT NULL  DEFAULT 0,
    "description" TEXT NOT NULL,
    "category_id" INT REFERENCES "blogcategory" ("id") ON DELETE SET NULL,
    "author_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "post" IS 'Articles class ';;
CREATE TABLE IF NOT EXISTS "comment" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "text" TEXT NOT NULL,
    "create_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "update_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "is_published" BOOL NOT NULL  DEFAULT True,
    "is_deleted" BOOL NOT NULL  DEFAULT False,
    "parent_id" INT REFERENCES "comment" ("id") ON DELETE SET NULL,
    "post_id" INT NOT NULL REFERENCES "post" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "comment" IS 'Comment class ';;
CREATE TABLE IF NOT EXISTS "tag" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50)  UNIQUE
);
COMMENT ON TABLE "tag" IS 'Tags class ';;
-- downgrade --
DROP TABLE IF EXISTS "blogcategory";
DROP TABLE IF EXISTS "comment";
DROP TABLE IF EXISTS "post";
DROP TABLE IF EXISTS "tag";
