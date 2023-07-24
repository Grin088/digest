INSERT INTO "users" (username, email, hashed_password) VALUES
('john', 'john@example.com', '$2b$12$E88kHmZmJ1gGzrnNAPtIL.uYtXAtowAgiey2QgJwgeT29T1TcvgvK'),
('jane', 'jane@example.com', '$2b$12$E88kHmZmJ1gGzrnNAPtIL.uYtXAtowAgiey2QgJwgeT29T1TcvgvK'),
('alex', 'alex@example.com', '$2b$12$E88kHmZmJ1gGzrnNAPtIL.uYtXAtowAgiey2QgJwgeT29T1TcvgvK')
ON CONFLICT DO NOTHING;

INSERT INTO "post_categories" (name) VALUES
('Sport'),
('Technologies'),
('Finance')
ON CONFLICT DO NOTHING;

INSERT INTO "post_categories" (name, parent_id)
SELECT 'skis', parent_id
FROM (SELECT id as parent_id FROM post_categories WHERE name = 'Sport') subquery
UNION
SELECT 'swiming', parent_id
FROM (SELECT id as parent_id FROM post_categories WHERE name = 'Sport') subquery
UNION
SELECT 'machines', parent_id
FROM (SELECT id as parent_id FROM post_categories WHERE name = 'Technologies') subquery
UNION
SELECT 'robots', parent_id
FROM (SELECT id as parent_id FROM post_categories WHERE name = 'Technologies') subquery
UNION
SELECT 'banking', parent_id
FROM (SELECT id as parent_id FROM post_categories WHERE name = 'Finance') subquery
UNION
SELECT 'stocks', parent_id
FROM (SELECT id as parent_id FROM post_categories WHERE name = 'Finance') subquery
ON CONFLICT DO NOTHING;

INSERT INTO "subscriptions" (user_id)
SELECT u.id
FROM users u
WHERE u.username IN ('john', 'jane', 'alex')
ON CONFLICT DO NOTHING;

INSERT INTO "subscription_category_association_table" (post_category_id, subscription_id)
SELECT pc.id, s.id
FROM "post_categories" pc
CROSS JOIN "subscriptions" s
JOIN "users" u ON s.user_id = u.id
WHERE (pc.name IN ('Sport', 'Technologies') AND u.username = 'john')
   OR (pc.name IN ('Sport', 'Finance') AND u.username = 'jane')
   OR (pc.name IN ('Sport', 'Finance', 'Technologies') AND u.username = 'alex')
ON CONFLICT DO NOTHING;



INSERT INTO "posts" (post_category_id, name, text, rating, views)
SELECT c.id, 'Sample Post', 'Some post about skis competitions.', 5, 100
FROM "post_categories" c
WHERE c.name = 'skis'
UNION
SELECT c.id, 'Sample Post', 'Some post about skis records.', 2, 200
FROM "post_categories" c
WHERE c.name = 'skis'
UNION
SELECT c.id, 'Sample Post', 'Some post about swimming competitions.', 3.5, 150
FROM "post_categories" c
WHERE c.name = 'swimming'
UNION
SELECT c.id, 'Sample Post', 'Some post about swimming records.', 2, 88
FROM "post_categories" c
WHERE c.name = 'swimming'
UNION
SELECT c.id, 'Sample Post', 'Some post about industrial machines', 5, 33
FROM "post_categories" c
WHERE c.name = 'machines'
UNION
SELECT c.id, 'Sample Post', 'Some post about parts for machines', 3.7, 218
FROM "post_categories" c
WHERE c.name = 'machines'
UNION
SELECT c.id, 'Sample Post', 'Some post about robotics.', 4, 200
FROM "post_categories" c
WHERE c.name = 'robots'
UNION
SELECT c.id, 'Sample Post', 'Some post about robotics innovations', 4.6, 316
FROM "post_categories" c
WHERE c.name = 'robots'
UNION
SELECT c.id, 'Sample Post', 'Some post about banking innovations', 3, 5
FROM "post_categories" c
WHERE c.name = 'banking'
UNION
SELECT c.id, 'Sample Post', 'Some post about banking alleges', 2, 125
FROM "post_categories" c
WHERE c.name = 'banking'
UNION
SELECT c.id, 'Sample Post', 'Some post about stocks', 5, 350
FROM "post_categories" c
WHERE c.name = 'stocks'
UNION
SELECT c.id, 'Sample Post', 'Some post about stocks trends', 5, 88
FROM "post_categories" c
WHERE c.name = 'stocks'
ON CONFLICT DO NOTHING;


