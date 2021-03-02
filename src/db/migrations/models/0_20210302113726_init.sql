-- upgrade --
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(100) NOT NULL UNIQUE,
    "email" VARCHAR(100) NOT NULL UNIQUE,
    "password" VARCHAR(100) NOT NULL,
    "first_name" VARCHAR(100) NOT NULL,
    "last_name" VARCHAR(100),
    "date_join" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "last_login" TIMESTAMPTZ,
    "is_active" BOOL NOT NULL  DEFAULT False,
    "is_staff" BOOL NOT NULL  DEFAULT False,
    "is_superuser" BOOL NOT NULL  DEFAULT False,
    "avatar" VARCHAR(100)
);
COMMENT ON TABLE "user" IS 'Model user';
CREATE TABLE IF NOT EXISTS "socialaccount" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "account_id" INT NOT NULL,
    "account_url" VARCHAR(500) NOT NULL,
    "account_login" VARCHAR(100) NOT NULL,
    "account_name" VARCHAR(100) NOT NULL,
    "provider" VARCHAR(100) NOT NULL,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "socialaccount" IS 'Model social accounts';
CREATE TABLE IF NOT EXISTS "verification" (
    "link" UUID NOT NULL  PRIMARY KEY,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "verification" IS 'Модель для подтверждения регистрации пользователя';
CREATE TABLE IF NOT EXISTS "category" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(150) NOT NULL,
    "parent_id" INT REFERENCES "category" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "category" IS 'Categories by project';
CREATE TABLE IF NOT EXISTS "toolkit" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(150) NOT NULL,
    "parent_id" INT REFERENCES "toolkit" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "toolkit" IS 'Toolkit by project';
CREATE TABLE IF NOT EXISTS "project" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(150) NOT NULL,
    "description" TEXT NOT NULL,
    "create_date" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "category_id" INT NOT NULL REFERENCES "category" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "toolkit_id" INT NOT NULL REFERENCES "toolkit" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "project" IS 'Model for project';
CREATE TABLE IF NOT EXISTS "task" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "description" TEXT NOT NULL,
    "create_date" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "start_date" TIMESTAMPTZ,
    "end_date" TIMESTAMPTZ,
    "project_id" INT NOT NULL REFERENCES "project" ("id") ON DELETE CASCADE,
    "worker_id" INT REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "task" IS 'Model task by project';
CREATE TABLE IF NOT EXISTS "commenttask" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "message" VARCHAR(1000) NOT NULL,
    "create_date" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "task_id" INT NOT NULL REFERENCES "task" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "commenttask" IS 'Model comment by task';
CREATE TABLE IF NOT EXISTS "blogcategory" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "published" BOOL NOT NULL  DEFAULT True,
    "description" TEXT NOT NULL,
    "parent_id" INT REFERENCES "blogcategory" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "blogcategory" IS 'Class category ';
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
    "author_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "category_id" INT REFERENCES "blogcategory" ("id") ON DELETE SET NULL
);
COMMENT ON TABLE "post" IS 'Articles class ';
CREATE TABLE IF NOT EXISTS "comment" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "text" TEXT NOT NULL,
    "create_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "update_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "is_published" BOOL NOT NULL  DEFAULT True,
    "is_deleted" BOOL NOT NULL  DEFAULT False,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "post_id" INT NOT NULL REFERENCES "post" ("id") ON DELETE CASCADE,
    "parent_id" INT REFERENCES "comment" ("id") ON DELETE SET NULL
);
COMMENT ON TABLE "comment" IS 'Comment class ';
CREATE TABLE IF NOT EXISTS "tag" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50)  UNIQUE
);
COMMENT ON TABLE "tag" IS 'Tags class ';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "team_project" (
    "project_id" INT NOT NULL REFERENCES "project" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "post_tag" (
    "post_id" INT NOT NULL REFERENCES "post" ("id") ON DELETE CASCADE,
    "tag_id" INT NOT NULL REFERENCES "tag" ("id") ON DELETE CASCADE
);
