<?php

namespace App\Http\Controllers;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Field_calculate;
use Illuminate\Support\Facades\Validator;


class CalculationController extends Controller
{
    public function calculate(Request $request){
        $validator = Validator::make($request->all(), [
            'expression' => [
                'required',
                function ($attribute, $value, $fail) {
                    if(!preg_match("#^[0-9 \.\+\-\*\/\(\)]+$#", $value)){
                        $fail('Expression includes unavailable character(s)!');
                    }
                    if (substr_count($value, '(') != substr_count($value, ')')) {
                        $fail('Parenthesis error!'); 
                    }
                },
            ],
        ],[
            'expression.required' => 'Please enter expression',
        ]);
        if ($validator->fails()) {
            $response = [
                'error' => $validator->errors()->all()[0]
            ];
            return response()->json($response, 404);
        }
        $calc = new Field_calculate();
        $res = $calc->calculate($request->get("expression"));
        $response = response()->json(['result' => $res]);
        return $response;
    }
}
