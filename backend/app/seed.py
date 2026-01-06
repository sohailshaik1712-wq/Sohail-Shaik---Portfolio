from app.database import SessionLocal
from app.models import Project

db = SessionLocal()

projects = [
    Project(
        slug="ai-translation-platform",
        title="AI Product Translation Platform",
        description="AI-powered multilingual enrichment system",
        image="/projects/mdm.png",
        tags="Azure AI,Stibo STEP,MDM,APIs",
        details="Built AI translation workflows integrated with Azure AI services to standardize multilingual product master data.",
    ),
    Project(
        slug="global-mdm-integration",
        title="Global MDM Integration Platform",
        description="Enterprise MDM ingestion & outbound integration",
        image="/projects/mdm.png",
        tags="SAP,Excel,REST APIs,Data Governance",
        details="Designed SAP and Excel ingestion pipelines and outbound REST integrations delivering datasets to SKUVantage (Australia).",
    ),
    Project(
        slug="data-quality-framework",
        title="Enterprise Data Quality Framework",
        description="Rule-based master data validation system",
        image="/projects/mdm.png",
        tags="Business Rules,Validation,MDM",
        details="Implemented centralized data quality rule engines enforcing completeness, uniqueness and consistency.",
    ),
    Project(
        slug="product-onboarding-workflows",
        title="Product Onboarding Automation",
        description="Workflow-driven global product onboarding",
        image="/projects/mdm.png",
        tags="Workflow Automation,Orchestration",
        details="Built automated onboarding workflows for multi-region product approval and publishing.",
    ),
    Project(
        slug="api-outbound-hub",
        title="Outbound API Integration Hub",
        description="Secure REST-based outbound delivery platform",
        image="/projects/mdm.png",
        tags="REST APIs,JSON,Security",
        details="Engineered centralized outbound APIs delivering validated product data to analytics platforms.",
    ),
    Project(
        slug="sap-excel-ingestion",
        title="SAP & Excel Ingestion Pipelines",
        description="Multi-source ingestion platform",
        image="/projects/mdm.png",
        tags="SAP,Excel,ETL",
        details="Designed automated ingestion pipelines supporting enterprise SAP systems and Excel bulk uploads.",
    ),
    Project(
        slug="mdm-governance-model",
        title="MDM Governance & Stewardship Model",
        description="Data governance & stewardship platform",
        image="/projects/mdm.png",
        tags="Governance,Stewardship",
        details="Implemented governance workflows ensuring compliance, ownership, and auditability of master data.",
    ),
    Project(
        slug="analytics-ready-modeling",
        title="Analytics Ready Data Modeling",
        description="Dimensional modeling for BI enablement",
        image="/projects/mdm.png",
        tags="Dimensional Modeling,BI",
        details="Designed star-schema dimensional models enabling enterprise BI and reporting workloads.",
    ),
    Project(
        slug="sku-optimization-platform",
        title="SKU Optimization & Rationalization",
        description="SKU lifecycle and duplication management",
        image="/projects/mdm.png",
        tags="SKU,Optimization",
        details="Built SKU duplication detection and lifecycle management pipelines improving catalog quality.",
    ),
    Project(
        slug="global-product-syndication",
        title="Global Product Syndication Platform",
        description="Cross-market product data syndication",
        image="/projects/mdm.png",
        tags="Syndication,Retail",
        details="Engineered global syndication pipelines delivering standardized datasets to external marketplaces.",
    ),
]

db.add_all(projects)
db.commit()
db.close()

print("Seed data inserted successfully.")
