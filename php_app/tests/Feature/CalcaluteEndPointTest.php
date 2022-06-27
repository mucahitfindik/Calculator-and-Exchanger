<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
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
        $response = $this->json('GET', "/calculate", ['expression' => "(2/4*(6-3))"]);

        $response->assertStatus(200);
    }
    public function test_has_expression_attribute()
    {
        $response = $this->json('GET', "/calculate");

        $this->assertEquals(json_decode($response->getContent())->message, "Expression Not Found!");
    }
    public function test_invalid_expression()
    {
        $response = $this->json('GET', "/calculate", ['expression' => "(2/4*(6-3)das)"]);

        $this->assertEquals(json_decode($response->getContent())->message, "Expression includes unavailable character(s)!");
    }
    public function test_parenthesis_error()
    {
        $response = $this->json('GET', "/calculate", ['expression' => "(2/4*(6-3)"]);

        $this->assertEquals(json_decode($response->getContent())->message, "Parenthesis error!");
    }
    public function test_checkResult(){
        $response = $this->json('GET', "/calculate",['expression' => "2+4+5"]);
        $this->assertEquals(json_decode($response->getContent())->result, 11);
    }
}
