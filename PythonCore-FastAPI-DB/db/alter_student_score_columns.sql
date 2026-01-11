/*
  ALTER TABLE script to widen student_score decimal columns from (3,2) to (5,2).
  Run this in SSMS or via sqlcmd while connected to the AI_Roadmap database.

  IMPORTANT: Back up the table before running. Test in a non-production environment first.
*/

USE [AI_Roadmap]
GO

ALTER TABLE dbo.student_score ALTER COLUMN tamil decimal(5,2) NOT NULL;
ALTER TABLE dbo.student_score ALTER COLUMN english decimal(5,2) NOT NULL;
ALTER TABLE dbo.student_score ALTER COLUMN maths decimal(5,2) NOT NULL;
ALTER TABLE dbo.student_score ALTER COLUMN science decimal(5,2) NOT NULL;
ALTER TABLE dbo.student_score ALTER COLUMN socail_science decimal(5,2) NOT NULL;
GO

/*
If you prefer a single transaction, wrap the changes as follows (SQL Server may not allow altering columns with FK dependencies inside a transaction):

BEGIN TRANSACTION;
ALTER TABLE dbo.student_score ALTER COLUMN tamil decimal(5,2) NOT NULL;
ALTER TABLE dbo.student_score ALTER COLUMN english decimal(5,2) NOT NULL;
ALTER TABLE dbo.student_score ALTER COLUMN maths decimal(5,2) NOT NULL;
ALTER TABLE dbo.student_score ALTER COLUMN science decimal(5,2) NOT NULL;
ALTER TABLE dbo.student_score ALTER COLUMN socail_science decimal(5,2) NOT NULL;
COMMIT TRANSACTION;

*/
