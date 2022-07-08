<?php

namespace Tests\Feature;

use Tests\TestCase;

class CalcaluteEndPointTest extends TestCase
{
    /**
     * A basic feature test example.
     *
     * @return void
     */
    public function test_endpoint_check()
    {
        $response = $this->json('POST', "/calculate", ['expression' => "(2/4*(6-3))"]);

        $response->assertStatus(200);
    }
    public function test_has_expression_attribute()
    {
        $response = $this->json('POST', "/calculate");

        $this->assertEquals(json_decode($response->getContent())->error, "Please enter expression");
    }
    public function test_invalid_expression()
    {
        $response = $this->json('POST', "/calculate", ['expression' => "(2/4*(6-3)das)"]);

        $this->assertEquals(json_decode($response->getContent())->error, "Expression includes unavailable character(s)!");
    }
    public function test_parenthesis_error()
    {
        $response = $this->json('POST', "/calculate", ['expression' => "(2/4*(6-3)"]);

        $this->assertEquals(json_decode($response->getContent())->error, "Parenthesis error!");
    }
    public function test_checkResult(){
        $response = $this->json('POST', "/calculate",['expression' => "2+4+5"]);
        $this->assertEquals(json_decode($response->getContent())->result, 11);
    }
}
