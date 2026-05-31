from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    text
)

from connect import Base


# =====================================================
# hamego_ci
# =====================================================
class CustomerInfo(Base):

    __tablename__ = "hamego_ci"

    cust_id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(255),
        nullable=False
    )

    email = Column(
        String(255),
        nullable=True
    )

    mobile = Column(
        String(20),
        nullable=True
    )

    line_id = Column(
        String(100),
        nullable=True
    )

    birth_month = Column(
        Integer,
        nullable=True
    )

    gender = Column(
        String(2),
        nullable=True
    )

    consent_marketing = Column(
        Boolean,
        nullable=True
    )

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )


# =====================================================
# hamego_event
# =====================================================
class Event(Base):

    __tablename__ = "hamego_event"

    event_id = Column(
        String(10),
        primary_key=True
    )

    cust_id = Column(
        Integer,
        nullable=False
    )

    event_type = Column(
        String(255),
        nullable=True
    )

    event_date = Column(
        DateTime,
        nullable=True
    )

    running = Column(
        Integer,
        nullable=True
    )

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )

    last_update = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )


# =====================================================
# hamego_pbmain
# =====================================================
class PhotoBoothMain(Base):

    __tablename__ = "hamego_pbmain"

    trans_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    session_id = Column(
        String(25),
        nullable=False
    )

    event_id = Column(
        String(10),
        nullable=False
    )

    type = Column(
        String(2),
        nullable=True
    )

    source = Column(
        String(255),
        nullable=True
    )

    download_url = Column(
        String(255),
        nullable=True
    )

    status_print = Column(
        Integer,
        server_default=text("0")
    )

    status_download = Column(
        Integer,
        server_default=text("0")
    )

    last_update = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )


# =====================================================
# hamego_printer_pool
# =====================================================
class PrinterPool(Base):

    __tablename__ = "hamego_printer_pool"

    print_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    session_id = Column(
        String(25),
        nullable=False
    )

    source_file = Column(
        String(255),
        nullable=True
    )

    print_status = Column(
        String(10),
        nullable=True
    )

    print_datetime = Column(
        DateTime,
        nullable=True
    )

    reprint_count = Column(
        Integer,
        server_default=text("0")
    )

    last_update = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )