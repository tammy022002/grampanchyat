from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "Admin"
    GRAMSEVAK = "Gramsevak"
    SARPANCH = "Sarpanch"
    ACCOUNTANT = "Accountant"
    AUDITOR = "Auditor"
    CLERK = "Clerk"
    DATA_ENTRY_OPERATOR = "Data Entry Operator"
    TALUKA_OFFICER = "Taluka Officer"
    DISTRICT_OFFICER = "District Officer"

class StatusEnum(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
