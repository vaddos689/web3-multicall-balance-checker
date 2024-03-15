from core.balance_checker import EvmBalanceChecker


MODULES = {
    1: ("balance_checker", EvmBalanceChecker),
}


def get_module(module):
    module_info = MODULES.get(module)
    if module_info:
        module_name, func = module_info

        return func, module_name
    else:
        raise ValueError(f"Unsupported module: {module}")


async def main(module):
    func, module_name = get_module(module)

    if module == 1:
        await func().start()
