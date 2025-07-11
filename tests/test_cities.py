"""
Tests for the cities API endpoint
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_cities_spain():
    """Test the cities endpoint with Spain as the country"""
    response = client.get("/cities/Spain")
    
    assert response.status_code == 200
    data = response.json()
    
    # Spain should return Seville
    assert "cities" in data
    assert data["cities"] == ["Seville"]


def test_get_cities_usa():
    """Test the cities endpoint with USA (existing country)"""
    response = client.get("/cities/USA")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "cities" in data
    assert data["cities"] == ["New York", "Los Angeles", "Chicago"]


def test_get_cities_canada():
    """Test the cities endpoint with Canada (existing country)"""
    response = client.get("/cities/Canada")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "cities" in data
    assert data["cities"] == ["Toronto", "Vancouver", "Montreal"]


def test_get_cities_uk():
    """Test the cities endpoint with UK (existing country)"""
    response = client.get("/cities/UK")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "cities" in data
    assert data["cities"] == ["London", "Manchester", "Birmingham"]


def test_get_cities_nonexistent_country():
    """Test the cities endpoint with a non-existent country"""
    response = client.get("/cities/Atlantis")
    
    assert response.status_code == 200
    data = response.json()
    
    # Non-existent countries should return empty list
    assert "cities" in data
    assert data["cities"] == []
