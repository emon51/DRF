import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from myapp.models import Product

# reverse: generate URL from name
# APIClient: simulate API requests


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def product(db):
    return Product.objects.create(
        name="Laptop",
        price=1200,
        description="Gaming Laptop"
    )


# GET ALL PRODUCTS
@pytest.mark.django_db
def test_get_products(api_client, product):
    url = reverse("product-list")

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == product.name


# CREATE PRODUCT
@pytest.mark.django_db
def test_create_product(api_client):
    url = reverse("product-list")

    data = {
        "name": "Phone",
        "price": 800,
        "description": "Smartphone"
    }

    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name"] == data["name"]
    assert Product.objects.count() == 1


# GET SINGLE PRODUCT
@pytest.mark.django_db
def test_get_product_detail(api_client, product):
    url = reverse("product-detail", args=[product.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == product.name


# UPDATE PRODUCT
@pytest.mark.django_db
def test_update_product(api_client, product):
    url = reverse("product-detail", args=[product.id])

    data = {
        "name": "Updated Laptop",
        "price": 1300,
        "description": "Updated description"
    }

    response = api_client.put(url, data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == "Updated Laptop"


# DELETE PRODUCT
@pytest.mark.django_db
def test_delete_product(api_client, product):
    url = reverse("product-detail", args=[product.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Product.objects.count() == 0


# VALIDATION TEST
@pytest.mark.django_db
def test_create_product_invalid(api_client):
    url = reverse("product-list")

    data = {
        "name": "",
        "price": "",
        "description": "Invalid"
    }

    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST