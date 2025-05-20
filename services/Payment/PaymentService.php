<?php


namespace App\Http\Services\Payment;

use Illuminate\Support\Facades\Config;

class PaymentService
{

    public function zarinpal($amount, $order, $onlinePayment)
    {
        $merchant_id = Config::get("payment.zarinpal_api_key");
        try {
            $response = zarinpal()
                ->merchantId($merchant_id) // تعیین مرچنت کد در حین اجرا - اختیاری
                ->amount($amount) // مبلغ تراکنش
                ->request()
                ->description('transaction info') // توضیحات تراکنش
                ->callbackUrl(route('customer.sales-process.payment-call-back', [$order, $onlinePayment])) // آدرس برگشت پس از پرداخت
                // ->mobile('09123456789') // شماره موبایل مشتری - اختیاری
                // ->email('ali@domain.com') 
                ->send();

            if (!$response->success()) {
                return $response->error()->message();
            } else {
                $onlinePayment->update(['bank_first_response' => ($response)]);
                $authority = $response->authority();
                return $response->redirect();
            }


            // ذخیره اطلاعات در دیتابیس
            // $response->authority();

        } catch (\Throwable $th) {
            return false;
        }
    }

    public function zarinpalVerify($amount, $onlinePayment)
    {
        $authority = request()->query('Authority'); // دریافت کوئری استرینگ ارسال شده توسط زرین پال
        $status = request()->query('Status'); // دریافت کوئری استرینگ ارسال شده توسط زرین پال
        $merchant_id = Config::get("payment.zarinpal_api_key");

        $response = zarinpal()
            ->merchantId($merchant_id) // تعیین مرچنت کد در حین اجرا - اختیاری
            ->amount($amount)
            ->verification()
            ->authority($authority)
            ->send();

        if (!$response->success()) {
            // return $response->error()->message();
            // return redirect()->route('customer.home')->with('danger', 'پرداخت ناموفق بود.');

            return ['success' => false];
        }
        
        $onlinePayment->update(['bank_secound_response' => $response]);
        return ['success' => true];
        // return redirect()->route('customer.home')->with('success', 'پرداخت شما موفقیت آمیز بود.');



        // دریافت هش شماره کارتی که مشتری برای پرداخت استفاده کرده است
        // $response->cardHash();

        // دریافت شماره کارتی که مشتری برای پرداخت استفاده کرده است (بصورت ماسک شده)
        // $response->cardPan();

        // پرداخت موفقیت آمیز بود
        // دریافت شماره پیگیری تراکنش و انجام امور مربوط به دیتابیس
        // return $response->referenceId();
    }
}
