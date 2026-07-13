import pytest
from datetime import datetime
from core.models import Trade
from core.enums import TradeDirection, TradePhase
from data.dhan_client import DhanClient
from unittest.mock import MagicMock

def test_trade_pnl_and_transaction_costs():
    # Setup trade with 2 lots (lot size = 65)
    # Entry premium sum: CE (100) + PE (100) = 200
    # Current premium sum: CE (110) + PE (105) = 215
    # Gross profit: (215 - 200) * 2 * 65 = 15 * 130 = ₹1950.00
    # Transaction costs: ₹103 per lot * 2 = ₹206.00
    # Net profit: ₹1950.00 - ₹206.00 = ₹1744.00
    trade = Trade(
        direction=TradeDirection.LONG_CE,
        strike_ce=24300,
        strike_pe=24300,
        entry_ce_price=100.0,
        entry_pe_price=100.0,
        quantity=2,
        lot_size=65,
        entry_time=datetime.now(),
        phase=TradePhase.PHASE_1_BOTH_LEGS,
        ce_current_price=110.0,
        pe_current_price=105.0
    )

    assert trade.gross_pnl == 1950.00
    assert trade.transaction_costs == 206.00
    assert trade.net_pnl == 1744.00


def test_dhan_client_validate_credentials_success():
    client = DhanClient()
    # Mock self.client.get_positions to return success
    client.client = MagicMock()
    client.client.get_positions.return_value = {"status": "success", "data": []}

    assert client.validate_credentials() is True


def test_dhan_client_validate_credentials_failure():
    client = DhanClient()
    client.client = MagicMock()
    client.client.get_positions.return_value = {
        "status": "failure",
        "remarks": {
            "error_code": "DH-901",
            "error_type": "Invalid_Authentication",
            "error_message": "Access token expired"
        }
    }

    with pytest.raises(ValueError, match="Dhan Access Token expired or invalid"):
        client.validate_credentials()
