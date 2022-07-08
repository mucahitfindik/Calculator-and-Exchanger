<?php

namespace Tests\Feature;

use Tests\TestCase;

class ErrorHandlerTest extends TestCase
{
    /**
     * A basic feature test example.
     *
     * @return void
     */
    public function test_not_allowed_method_calulate()
    {
        $response = $this->json('GET', "/calculate", ['expression' => "(2/4*(6-3))"]);

        $this->assertEquals(json_decode($response->getContent())->error, "The method is not allowed for the requested URL.");
    }
    public function test_not_defined_end_point()
    {
        $response = $this->json('GET', "/calculat", ['expression' => "(2/4*(6-3))"]);

        $this->assertEquals(json_decode($response->getContent())->error, "The requested URL was not found on the server.");
    }
}
