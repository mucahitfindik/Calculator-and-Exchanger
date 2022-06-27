<?php

namespace Tests\Unit;

use PHPUnit\Framework\TestCase;
use App\Models\Field_calculate;
class FieldCalculateTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    private $calc;

    protected function setUp(): void
    {
        $this->calc = new Field_calculate();
    }
    public function test_field_calculate_simple()
    {
        $exp = 2*5;
        $res = $this->calc->calculate($exp);
        $this->assertEquals($res, 10);

    }
    public function test_field_calculate_with_parenthesis()
    {
        $exp = (2*5);
        $res = $this->calc->calculate($exp);
        $this->assertEquals($res, 10);

    }
    public function test_field_calculate_mix()
    {
        $exp = (2/4*(6-3));
        $res = $this->calc->calculate($exp);
        $this->assertEquals($res, 1.5);

    }
}
